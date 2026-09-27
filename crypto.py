
import sys
import caesar
import affine
import argparse
import vigenere
import monoalpha
from assist import report
from break_caesar import break_caesar
from break_affine import break_affine
from break_vigenere import break_vigenere

def read_input(args) -> str:
    if args.in_file:
        with open(args.in_file, 'r') as f:
            return f.read()
    return sys.stdin.read()

def write_output(args, text: str) -> None:
    if args.out_file:
        with open(args.out_file, 'w') as f:
            f.write(text)
    else:
        print(text)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="crypto.py")
    subparsers = parser.add_subparsers(dest="cipher", required = True)

    caesar_parser = subparsers.add_parser("caesar")
    caesar_parser.add_argument("mode", choices= ["encrypt", "decrypt"])
    caesar_parser.add_argument("--key", type = int, required = True)
    caesar_parser.add_argument("--in", dest = 'in_file', default = None)
    caesar_parser.add_argument("--out", dest = 'out_file', default = None)

    affine_parser = subparsers.add_parser("affine")
    affine_parser.add_argument("mode", choices= ["encrypt", "decrypt"])
    affine_parser.add_argument("--a", type = int, required = True)
    affine_parser.add_argument("--b", type = int, required = True)
    affine_parser.add_argument("--in", dest = 'in_file', default = None)
    affine_parser.add_argument("--out", dest = 'out_file', default = None)

    mono_parser = subparsers.add_parser("mono")
    mono_parser.add_argument("mode", choices= ["encrypt", "decrypt"])
    mono_parser.add_argument("--key", type = str)
    mono_parser.add_argument("--keyword", type = str)
    mono_parser.add_argument("--in", dest = 'in_file', default = None)
    mono_parser.add_argument("--out", dest = 'out_file', default = None)

    vig_parser = subparsers.add_parser("vigenere")
    vig_parser.add_argument("mode", choices = ["encrypt", "decrypt"])
    vig_parser.add_argument("--key", type = str, required = True)
    vig_parser.add_argument("--in", dest= "in_file", default = None)
    vig_parser.add_argument("--out", dest= "out_file", default = None)

    break_parser = subparsers.add_parser("break")
    break_parser.add_argument("target", choices = ["caesar", "affine", "vigenere"])
    break_parser.add_argument("--m", type = int)
    break_parser.add_argument("--in", dest = "in_file", default = None)
    break_parser.add_argument("--out", dest = "out_file", default = None)
    break_parser.add_argument("--lang", default = "en")

    assist_parser = subparsers.add_parser("assist")
    assist_parser.add_argument("--in", dest= "in_file", default = None)
    assist_parser.add_argument("--out", dest= "out_file", default = None)
    assist_parser.add_argument("--lang", default = "en")

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.cipher == "caesar":
            text = read_input(args)
            if args.key is None:
                raise ValueError("caesar requires key.")
                
            if args.mode == "encrypt":
                write_output(args, caesar.encrypt(text, args.key))
            else:
                write_output(args, caesar.decrypt(text, args.key))

        elif args.cipher == "affine":
            text = read_input(args)
            if args.a is None or args.b is None:
                raise ValueError("affine requires a & b.")
                
            if args.mode == "encrypt":
                write_output(args, affine.encrypt(text, args.a, args.b))
            else:
                write_output(args, affine.decrypt(text, args.a, args.b))

        elif args.cipher == "mono":
            text = read_input(args)
            if args.keyword:
                key = monoalpha.key_from_keyword(args.keyword)
            elif args.key:
                key = args.key
            else:
                raise ValueError("mono requires a key or keyword")
                
            if args.mode == "encrypt":
                write_output(args, monoalpha.encrypt(text,key))
            else:
                write_output(args, monoalpha.decrypt(text,key))

        elif args.cipher == "vigenere":
            text = read_input(args)
            if args.key is None:
                raise ValueError("vigenere requires key")
                
            if args.mode == "encrypt":
                write_output(args, vigenere.encrypt(text, args.key))
            else:
                write_output(args, vigenere.decrypt(text, args.key))

        elif args.cipher == "break":
            text = read_input(args)
            
            if args.target == "caesar":
                k, plain = break_caesar(text, args.lang)
                write_output(args, f"k={k}\n{plain}")
                
            elif args.target == "affine":
                key, plain = break_affine(text, args.lang)
                write_output(args, f"key={key}\n{plain}")

            elif args.target == "vigenere":
                if args.m is None:
                    raise ValueError("break vigenererequires m")
                key, plain = break_vigenere(text, args.m, args.lang)
                write_output(args, f"k={key}\n{plain}")

            elif args.cipher == "assist":
                text = read_input(args)
                write_output(args, report(text, args.lang))

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Error: File not found: {e.filename}", file = sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
                

    
    
    