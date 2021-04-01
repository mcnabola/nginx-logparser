import time

def watch(fn, words):
    fp = open(fn, 'r')
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            print(new)
            for word in words:
                if word in new:
                    yield (word, new)
        else:
            print("SLEEP")
            time.sleep(4)

fn = 'accesslog.txt'
words = ['word']
for hit_word, hit_sentence in watch(fn, words):
    print ("Found %r in line: %r" % (hit_word, hit_sentence))
