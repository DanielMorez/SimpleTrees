from xml.etree import ElementTree as ET


max_depth = 0


def depth_iter(element, tag=None):
    global max_depth

    stack = [iter([element])]
    while stack:
        e = next(stack[-1], None)
        if e is None:
            stack.pop()
        else:
            stack.append(iter(e))
            if tag is None or e.tag == tag:
                if max_depth < len(stack) - 1:
                    max_depth = len(stack) - 1
                yield e, len(stack) - 1


if __name__ == '__main__':
    while True:
        xml = input()
        try:
            root_node = ET.parse(xml if xml else 'sample.xml').getroot()
            depth_iter(root_node)  # Пробегаем по всем узлам дерева
            print(max_depth - 1)
        except:
            print('break? (y/n)')
            if input().lower() in ('yes', 'y'):
                break
