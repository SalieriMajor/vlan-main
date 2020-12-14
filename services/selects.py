from models import Vlan
from logging_handlers import create_logger


def get_all_vlans():
    logger = create_logger('get_vlans')
    logger.debug('getting all vlans')
    vlans = Vlan.query.order_by(Vlan.id).all()
    logger.debug('vlans fetched successully')
    return vlans

