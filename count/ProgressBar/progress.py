import sys, traceback, time

class progress(object):
    iteration = 0
    total = 100
    prefix = ''
    suffix = ''
    decimals = 2
    barLength = 10
    startTime = time.time()

    def __init__(self, current_iteration, total_iterations, prefix_info = '',
                 suffix_info = '', num_decimals = 2, length = 10):
        self.iteration = current_iteration
        self.total = total_iterations
        self.prefix = prefix_info
        self.suffix = suffix_info
        self.decimals = num_decimals
        self.barLength = length
        self.start_time = time.time()
    
    def setTotalIterations(self, total_iterations):
        self.total = total_iterations

    def setDisplay(self, num_decimals = 2, length = 100):
        self.decimals = num_decimals
        self.barLength = length        
    
    def setCurrentIteration(self, current_iteration):
        self.iteration = current_iteration
    
    def setInfo(self, prefix_info = '', suffix_info = ''):
        if(prefix_info != ''):
            self.prefix = prefix_info
        if(suffix_info != ''):
            self.suffix = suffix_info

    def setStartTime(self, start_time):
        self.startTime = start_time

    def printProgress(self):
        filledLength    = int(round(self.barLength * self.iteration / 
                              float(self.total)))
        percents        = round(100.00 * (self.iteration / float(self.total)),
                                self.decimals)
        bar             = '+' * filledLength + ' ' * (self.barLength
                                                      - filledLength)
        past_time       = time.time() - self.startTime
        pastTime        = time.strftime("%H:%M:%S",
                          time.gmtime(time.time() - self.startTime))

        if(self.iteration == 0):
            remainTime  = 'N/A'
        else:
            remainTime  = time.strftime("%H:%M:%S",
                          time.gmtime(past_time/self.iteration*
                                     (self.total-self.iteration)))

        sys.stdout.write('%s [%s] %s%s [%s|%s] %s\r' % (self.prefix, bar,
                         percents, '%', pastTime, remainTime, self.suffix)),
        sys.stdout.flush()
        if self.iteration == self.total:
            print("\n")

def main():
    try:
        n = 1000
        test = progress(0,n)        
        for i in range(n):
            test.setCurrentIteration(i+1)
            test.setInfo(prefix_info = 'Processing ... ',
                         suffix_info = 'Iteration '+str(i)+'/'+str(n))
            test.printProgress()
            time.sleep(0.1)
           
    except KeyboardInterrupt:
        print "Shutdown requested... exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == '__main__':
    main()
