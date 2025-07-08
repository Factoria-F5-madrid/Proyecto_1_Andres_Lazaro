import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Handler para consola
        console_handler = logging.StreamHandler()
        simple_format = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(simple_format)
        logger.addHandler(console_handler)

        # Handler para archivo
        file_handler = logging.FileHandler('taximetro.log', encoding='utf-8')
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

        logger.propagate = False

    return logger
