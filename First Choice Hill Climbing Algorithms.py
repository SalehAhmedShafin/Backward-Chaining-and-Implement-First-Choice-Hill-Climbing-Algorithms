import random

def atd(id, status, state, hv):
  ts = []
  ts.append(id)
  ts.append(status)
  ts.append(state)
  ts.append(hv)
  database.append(ts)

def fhv(s):
    h = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                h += 1
            elif abs(s[i] - s[j]) == abs(i - j):
                h += 1
    return h 

def gs(s):
    success = []
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] != j:
                ns = s.copy()
                ns[i] = j
                success.append(ns)
    return success

def fchc(id, ss, sv):
    cs = ss
    cv = sv
    while True:
        successorst = gs(cs)
        fb = 0
        for ssv in successorst:
            sv = fhv(ssv)
            if sv < cv:
                id = id + 1
                atd(id, "c", ssv, sv)
                cs = ssv
                cv = sv
                fb = 1
                break
            else:
              id = id + 1
              atd(id, "s", ssv, sv)
        if not fb:
          if cv != 0:
            cs = [random.randint(0, 7) for i in range(8)]
            cv = fhv(cs)
          else:
            return 

ss = [2,3,4,5,6,5,7,8]
sv = fhv(ss)

database = []
atd(1, "c", ss,sv)

fchc(1, ss, sv)

print("All Current States: ")
for data in database:
  if data[1] == "c":
    print(data)