#------------------------------------------------------------------------------
# Copyright (c) 2013-2024, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
#------------------------------------------------------------------------------
from atom.api import Atom, AtomMeta, ChangeType, DefaultValue, Member, Typed

# The declarative engine only updates for these types of changes
D_CHANGE_TYPES = (
    ChangeType.UPDATE | ChangeType.PROPERTY | ChangeType.EVENT | ChangeType.DELETE
)


class DeclarativeDefaultHandler(Atom):
    """ A callable object which handles Declarative default values.

    This handler attempts to read the default value from the declarative
    engine, falling back on the default delegate if the engine does not
    have an implemented reader. Instances of this handler are created
    and installed by the DeclarativeMeta class.

    """
    delegate = Typed(Member, ())

    def __call__(self, owner, name):
        """ Invoke the declarative default handler.

        Parameters
        ----------
        owner : Declarative
            The declarative owner for which the default value should
            be computed.

        name : str
            The name of the attribute which should be read from the
            declarative engine.

        Returns
        -------
        result : object
            The default value for the object.

        """
        engine = owner._d_engine
        if engine is not None:
            value = engine.read(owner, name)
            if value is not NotImplemented:
                return value
        return self.delegate.do_default_value(owner)


def declarative_change_handler(change):
    """ A static observer which writes to a declarative engine.

    This handler will write the change to the declarative engine
    so that the engine can notify any bound expressions. This handler
    is attached by the DeclarativeMeta class.

    Parameters
    ----------
    change : dict
        The change dictionary generated by the notification.

    """
    # TODO think about whether this is the right place to filter on change_t
    # NOTE: Filtering on change['type'] is done by atom
    owner = change['object']
    engine = owner._d_engine
    if engine is not None:
        engine.write(owner, change['name'], change)


def patch_d_member(member):
    """ Patch the d_ member for declarative handling.

    This function will add the default value and change handlers to
    pull data from the declarative engine.

    Parameters
    ----------
    member : Member
        A member declared as a d_ member.

    """
    metadata = member.metadata
    if metadata['d_writable']:
        handler = DeclarativeDefaultHandler()
        handler.delegate = member.clone()
        new_mode = DefaultValue.CallObject_ObjectName
        member.set_default_value_mode(new_mode, handler)
    if metadata['d_readable']:
        member.add_static_observer(declarative_change_handler, D_CHANGE_TYPES)


class DeclarativeMeta(AtomMeta):
    """ The metaclass for Declarative classes.

    This metaclass patches up the default value handlers and default
    static observers based on the 'd_' members defined on the class.
    The patching must be done after the parent metaclass runs, since
    the bindings for the default engine must occur after the standard
    default handler hookups.

    """
    #: A flag which can be set on a declarative class to indicate to
    #: the compiler that instances of the class will build out their
    #: children. If this flag is set, the class must provide a method
    #: named 'child_node_intercept' which accepts the list of nodes
    #: and the local scope for their instantiation and returns None.
    __intercepts_child_nodes__ = False

    def __new__(meta, name, bases, dct):
        """ Create a new Declarative subclass.

        """
        # Create the subclass then pass over it's update dict and
        # patch up the default value and static change handlers for
        # the d_ members. This must done *after* the main metaclass
        # runs, or the declarative default values can get clobbered.
        cls = AtomMeta.__new__(meta, name, bases, dct)
        for key, value in cls.__dict__.items():
            if isinstance(value, Member):
                metadata = value.metadata
                if metadata is not None and metadata.get('d_member'):
                    patch_d_member(value)
        return cls
