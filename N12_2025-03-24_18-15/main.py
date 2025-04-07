import logging


def log():
    i = 0
    while i < 10:
        logging.warning(i)
        i += 1


def log2():
    logging.debug("Debug")
    logging.info("Info")
    logging.warning("Warning")
    logging.error("Error")
    logging.critical("Critical")

if __name__ == '__main__':
    logging.basicConfig(
        filename="arbuz2.log",
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        level=logging.DEBUG
    )
    log2()
