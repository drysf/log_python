from log import setup_logger


def ma_fonction():
    mon_logger = setup_logger()
    mon_logger.info("Message depuis mon_logger personnalisé")

ma_fonction()