# demonstrate the logging api in Python
import logging

# TODO: use the built-in logging module

def main():
    # TODO: Use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG, filemode="w", filename="output.log")
    # Try out each of the log levels
    logging.debug("Das ist eine Debug-Nachricht")
    logging.info("Das ist eine Info-Nachricht")
    logging.warning("Das ist eine Warning-Nachricht")
    logging.error("Das ist eine Error-Nachricht")
    logging.critical("Das ist eine Critical-Nachricht")
    logging.info("Hier ist eine {} variable und ein int: {}".format("string", 10))
    # TODO: Output formatted strings to the log


if __name__ == "__main__":
    main()
