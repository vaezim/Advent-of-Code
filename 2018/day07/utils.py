
class Scheduler:
    def __init__(self, text):
        self.jobs = {} # job -> set(required_jobs)
        self.completed_jobs = set()
        self._ProcessText(text)

    def GetMultiWorkerOrder(self, num_workers):
        time = 0
        self.completed_jobs.clear()
        workers = [] # len(workers) <= num_workers
        while len(self.completed_jobs) < len(self.jobs):
            ready_jobs = sorted(self._GetJobsWithNoDependency(workers))
            for job in ready_jobs:
                if len(workers) == num_workers:
                    break
                workers.append([job, self._GetJobTime(job)])
            workers.sort(key=lambda x: x[1], reverse=True) # Slowest to Fastest job
            finished_job = workers.pop()
            self.completed_jobs.add(finished_job[0])
            time += finished_job[1]
            for i in range(len(workers)):
                workers[i][1] -= finished_job[1]
        return time

    def GetSingleWorkerOrder(self):
        order = ""
        while len(self.completed_jobs) < len(self.jobs):
            next_job = min(self._GetJobsWithNoDependency())
            self.completed_jobs.add(next_job)
            order += next_job
        return order

    def _GetJobTime(self, job):
        return ord(job) - ord('A') + 61

    def _GetJobsWithNoDependency(self, workers=[]):
        jobs = []
        for job in self.jobs.keys():
            # Is completed
            if job in self.completed_jobs:
                continue
            # Is handed to worker
            is_handed_to_worker = False
            for work in workers:
                if work[0] == job:
                    is_handed_to_worker = True
                    break
            if is_handed_to_worker:
                continue
            satisfied = True
            for dep in self.jobs[job]:
                if dep not in self.completed_jobs:
                    satisfied = False
                    break
            if satisfied:
                jobs.append(job)
        return jobs

    def _ProcessText(self, text: list):
        for line in text:
            parent, child = line.split()[1], line.split()[-3]
            if self.jobs.get(parent) == None:
                self.jobs[parent] = set()
            if self.jobs.get(child) == None:
                self.jobs[child] = set()
            self.jobs[child].add(parent)