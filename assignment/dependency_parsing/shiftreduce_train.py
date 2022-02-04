
def makefeatures(stack, queue):
    feature = {}
    w2 = stack[-2]
    w1 = stack[-1]
    w0 = queue[0]
    label = f'{w2} {w1} {w0}'
    feature[label] = 1
    return feature


def shiftreduce(queue):
    heads = []
    stack = [(0, 'ROOT', 'ROOT')]
    while len(queue) > 0 or len(stack) > 1:
        features = makefeatures(stack, queue)
        label = str(features.keys())
        feature = int(features.values())
        weight_shift = weight_shift_dict.get(label, 0)
        weight_left = weight_left_dict.get(label, 0)
        weight_right = weight_right_dict.get(label, 0)
        score_shift = weight_shift * features
        score_left = weight_left * features
        score_right = weight_right * features
        if (score_shift >= score_left) and (score_shift >= score_right) and len(queue) > 0:
            stack.append(queue.pop(0))
        elif score_left >= score_right:
            heads[stack.index(stack[-2])] = stack.index(stack[-1])
            stack.del(-2)
        else:
            heads[stack.index(stack[-1])] = stack.index(stack[-2])
            stack.del(-1)
    
