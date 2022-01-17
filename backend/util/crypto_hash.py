import hashlib
import json

def crypto_hash(*args):

    stringified_args=sorted(map(lambda data: json.dumps(data),args))

    print(f'stringified_args: {args}')

    joined_data=''.join(stringified_args)
      
    print(f'joined_data:{joined_data}')

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one',2,[3]):{crypto_hash('one',2,[3])}")
    print(f"crypto_hash(1,'two',[3]):{crypto_hash(1,'two',[3])}")
    print(f"crypto_hash(1,2,[3]):{crypto_hash(1,2,[3])}")


if __name__== "__main__":
    main()