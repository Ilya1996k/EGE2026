n=0
for a1 in "акмс":
    for a2 in "акмс":
        for a3 in "акмс":
            for a4 in "акмс":
                for a5 in "акмс":
                    for a6 in "акмс":
                        s=a1+a2+a3+a4+a5+a6
                        n+=1
                        if s.count("с")==0 and s.count("м")==0 and s.count("кк")==0:
                            print(s,n)
