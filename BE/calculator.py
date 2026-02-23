import sys
import argparse
from calculator_helper import CalculatorHelper
import calculator_rest_service

def main():
    parser = argparse.ArgumentParser(prog='ProgramName',
          formatter_class=argparse.RawDescriptionHelpFormatter,
          epilog=('''Example of usage: python calculator.py --add 1 2'''))

    parser.add_argument('--port', type=int, default=5001, help='Port for REST API')

    parser.add_argument('-a', '--add', nargs='+', type=float, help='Add two numbers.')
    parser.add_argument('-s', '--subtract', nargs='+', type=float, help='Subtract two numbers.')
    parser.add_argument('-m', '--multiply', nargs='+', type=float, help='Multiply two numbers.')
    parser.add_argument('-d', '--divide', nargs='+', type=float, help='Divide two numbers.')
    parser.add_argument('-r', '--rest', action='store_true', help='Start REST service.')

    args = parser.parse_args()

    if not args.rest and len(sys.argv) != 4:
        print("Wrong number of arguments provided!\n")
        parser.print_help()
        sys.exit()

    if args.rest:
        calculator_rest_service.main(args)
    elif args.add:
        result = CalculatorHelper().add(args.add[0], args.add[1])
        print(f'{args.add[0]}+{args.add[1]}={result}')
    elif args.subtract:
        result = CalculatorHelper().subtract(args.subtract[0], args.subtract[1])
        print(f'{args.subtract[0]}-{args.subtract[1]}={result}')
    elif args.multiply:
        result = CalculatorHelper().multiply(args.multiply[0], args.multiply[1])
        print(f'{args.multiply[0]}*{args.multiply[1]}={result}')
    elif args.divide:
        result = CalculatorHelper().divide(args.divide[0], args.divide[1])
        print(f'{args.divide[0]}/{args.divide[1]}={result}')

if __name__ == '__main__':
    main()