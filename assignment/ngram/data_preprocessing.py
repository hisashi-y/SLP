with open('train.txt', 'r') as f:
        test = f.read()

test = test.replace('-', ' ')

with open('train_processed.txt', 'w') as f:
    f.write(test)
