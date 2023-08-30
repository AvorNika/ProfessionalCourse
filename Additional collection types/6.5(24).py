def best_sender(messages, senders):
    from collections import defaultdict
    data = defaultdict(int)

    for i in range(len(senders)):
        data[senders[i]] += len(messages[i].split())
    print(data)

    return max(data, key=lambda x: data[x])


messages = ['Hello userTwooo', 'Hi userThree', 'Wonderful day Alice', 'Nice day userThree']
senders = ['Alice', 'userTwo', 'userThree', 'Alice']

print(best_sender(messages, senders))