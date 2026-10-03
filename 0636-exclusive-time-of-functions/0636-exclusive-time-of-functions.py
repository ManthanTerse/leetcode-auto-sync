class Solution(object):
    def exclusiveTime(self, n, logs):
        exec_times = [0] * n
        stack = []
        for log in logs:
            i, status, timestamp = log.split(":")
            i, timestamp = int(i), int(timestamp)
            if status == "start":
                stack.append((i, timestamp))
            else:
                i, start = stack.pop()
                exec_times[i] += timestamp - start + 1
                if stack:
                    exec_times[stack[-1][0]] -= timestamp - start + 1
        return exec_times
        