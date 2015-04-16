
if __name__ == "__main__":
  dic = {}
  count = {}
  for i in range(1, 23):
    with open("../tpch-profile-icc/tpch-q%s.log" % i, "r") as in1:
      with open("../tpch-profile-gcc/tpch-q%s.log" % i, "r") as in2: 
        lines1 = in1.readlines()
        lines2 = in2.readlines()
        '''
        assert len(lines1)==len(lines2)
        '''
        length = len(lines1)
        collect = False
        for j in range(0, length):
          if j > 0 and "Operator" in lines1[j - 1]:
            collect = True
            continue
          if "Planner Timeline" in lines1[j]:
            collect = False
            break
          if collect:
            pos1 = lines1[j].index(":")
            pos2 = lines1[j].index("  ", pos1)
            key = lines1[j][pos1+1:pos2]
            avgtimes = lines1[j][pos2:].split()[1]
            avgtime = 0
            if "us" in avgtimes:
              if "ms" in avgtimes[:-2]:
                mspos = avgtimes[:-2].index("ms")
                if "s" in avgtimes[:mspos]:
                  spos = avgtimes[:mspos].index("s")
                  avgtime = avgtime + float(avgtimes[:spos]) * 1000 * 1000
                  avgtimes = avgtimes[spos+1:]
                mspos = avgtimes[:-2].index("ms")
                avgtime =avgtime + float(avgtimes[:mspos]) * 1000
                avgtimes = avgtimes[mspos+2:]
              avgtime = avgtime + float(avgtimes[:-2])
            elif "ms" in avgtimes:
                if "s" in avgtimes[:-2]:
                  spos = avgtimes[:-2].index("s")
                  avgtime = avgtime + float(avgtimes[:spos]) * 1000 * 1000
                  avgtimes = avgtimes[spos+1:]
                avgtime =avgtime + float(avgtimes[:-2]) * 1000
            elif "s" in avgtimes:
              avgtime = avgtime + float(avgtimes[:-2]) * 1000 * 1000

            avgtime1 = avgtime
            avgtimes = lines2[j][pos2:].split()[1]
            avgtime = 0
            if "us" in avgtimes:
              if "ms" in avgtimes[:-2]:
                mspos = avgtimes[:-2].index("ms")
                if "s" in avgtimes[:mspos]:
                  spos = avgtimes[:mspos].index("s")
                  avgtime = avgtime + float(avgtimes[:spos]) * 1000 * 1000
                  avgtimes = avgtimes[spos+1:]
                mspos = avgtimes[:-2].index("ms")
                avgtime =avgtime + float(avgtimes[:mspos]) * 1000
                avgtimes = avgtimes[mspos+2:]
              avgtime = avgtime + float(avgtimes[:-2])
            elif "ms" in avgtimes:
                if "s" in avgtimes[:-2]:
                  spos = avgtimes[:-2].index("s")
                  avgtime = avgtime + float(avgtimes[:spos]) * 1000 * 1000
                  avgtimes = avgtimes[spos+1:]
                avgtime =avgtime + float(avgtimes[:-2]) * 1000
            elif "s" in avgtimes:
              avgtime = avgtime + float(avgtimes[:-2]) * 1000 * 1000

            avgtime2 = avgtime

            if dic.has_key(key):
              if avgtime1 <> 0:
                dic[key] = dic[key] + avgtime2 * 100 / avgtime1
                count[key] = count[key] + 1
            else:
              if avgtime1 <> 0:
                dic[key] = avgtime2 * 100 / avgtime1
                count[key] = 1

  print sorted(dic.items(), key=lambda d: d[1])
  print (count)
