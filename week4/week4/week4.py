import heapq


class TriageSystem:
    def __init__(self, max_patients=100):
        self.queue = []
        self.next_id = 1
        self.called = []
        self.max_patients = max_patients
        self.queue_number = 0

    def add_patient(self, name, is_emergency=False, emergency_level=0):
        if len(self.queue) >= self.max_patients:
            print("排队已满，请稍后再来")
            return False

        patient_id = self.next_id
        self.next_id += 1
        self.queue_number += 1

        patient = {
            'id': patient_id,
            'name': name,
            'is_emergency': is_emergency,
            'emergency_level': emergency_level,
            'queue_number': self.queue_number
        }

        heapq.heappush(self.queue, (self.get_priority(patient), patient))
        print(f"{name} 排队成功，号码: {self.queue_number}")
        return True

    def get_priority(self, patient):
        if patient['is_emergency']:
            return (0, patient['emergency_level'], patient['queue_number'])
        else:
            return (1, patient['queue_number'])

    def call_next(self):
        if not self.queue:
            print("没有患者在排队")
            return None

        _, patient = heapq.heappop(self.queue)
        self.called.append(patient)
        print(f"请 {patient['name']} 到诊室就诊")
        return patient

    def show_queue(self):
        print("\n=== 当前排队情况 ===")
        print(f"排队人数: {len(self.queue)}/{self.max_patients}")
        print(f"已就诊: {len(self.called)}人")
        print(f"当前号码: {self.queue_number}")

        if not self.queue:
            print("没有人在排队")
            return

        print("\n排队列表:")
        temp_queue = self.queue.copy()
        temp_list = []

        while temp_queue:
            _, patient = heapq.heappop(temp_queue)
            temp_list.append(patient)

        for i, patient in enumerate(temp_list, 1):
            if patient['is_emergency']:
                print(f"{i}. {patient['name']} (急诊{patient['emergency_level']}) 号码:{patient['queue_number']}")
            else:
                print(f"{i}. {patient['name']} 号码:{patient['queue_number']}")

    def find_patient_position(self, patient_id):
        temp_queue = self.queue.copy()
        temp_list = []

        while temp_queue:
            _, patient = heapq.heappop(temp_queue)
            temp_list.append(patient)

        for i, patient in enumerate(temp_list, 1):
            if patient['id'] == patient_id:
                return i
        return None

    def remove_patient(self, patient_id):
        new_queue = []
        found = False

        for priority, patient in self.queue:
            if patient['id'] != patient_id:
                heapq.heappush(new_queue, (priority, patient))
            else:
                found = True
                print(f"{patient['name']} 已取消排队")

        self.queue = new_queue
        return found


def main():
    hospital = TriageSystem(max_patients=10)

    print("=== 医院排队系统 ===")

    hospital.add_patient("张三")
    hospital.add_patient("李四")
    hospital.add_patient("王五", True, 1)
    hospital.add_patient("赵六")
    hospital.add_patient("钱七", True, 2)

    print("\n当前排队:")
    hospital.show_queue()

    print("\n开始叫号:")
    hospital.call_next()
    hospital.call_next()

    print("\n叫号后:")
    hospital.show_queue()

    hospital.add_patient("孙八", True, 1)
    hospital.add_patient("周九")

    pos = hospital.find_patient_position(6)
    if pos:
        print(f"\n周九排在: 第{pos}位")

    print("\n继续叫号:")
    hospital.call_next()

    print("\n最终状态:")
    hospital.show_queue()


if __name__ == "__main__":
    main()