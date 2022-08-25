import attr

from ..factory import target_factory
from .common import Resource


@target_factory.reg_resource
@attr.s(eq=False)
class S2PiRelay(Resource):
    """This resource describes a S2Pi relay hat for power switching

    Args:
        busnum (int): i2c bus board is on
        devnum (int): i2c address for the board
        index (int): port index"""

    busnum = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(int)))
    devnum = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(int)))
    index = attr.ib(default=1, validator=attr.validators.instance_of(int))
