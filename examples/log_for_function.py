import logging

from traceback_with_variables import prints_exc, LoggerAsFile


logging.basicConfig(format='%(asctime)-15s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)


@prints_exc(file_=LoggerAsFile(logger))
def f(n):
    print(1 / n)


def main():
    f(0)


main()
