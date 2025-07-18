import argparse
from bookforge_core import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="BookForge Pro CLI")
    parser.add_argument("--topic", required=True, help="Book topic")
    parser.add_argument("--words", type=int, default=30000, help="Word count")
    parser.add_argument("--audiobook", choices=["yes","no"], default="no", help="Generate audiobook?")
    parser.add_argument("--export", default="pdf,epub", help="Export formats")
    args = parser.parse_args()
    run_pipeline(args.topic, args.words, args.audiobook, args.export.split(","))

if __name__ == "__main__":
    main()
