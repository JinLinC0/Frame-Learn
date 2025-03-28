public class MiGong {
	public static void main(String[] args) {
		// ��ʼ���Թ�����״
		int [][] map = new int [8][7];

		// ��������һ�к�������һ�У�ȫ������Ϊ1
		for(int i = 0; i < 7; i++) {
			map[0][i] = 1;   // ������һ��
			map[7][i] = 1;   // ������һ��
		}

		// �����һ�к����һ�У�ȫ������Ϊ1
		for(int i = 0; i < 8; i++) {
			map[i][0] = 1;   // �����һ��
			map[i][6] = 1;   // ���ұ�һ��
		}

		// ��[3][1]��[3][2]��[2][2]λ������Ϊ1
		map[3][1] = 1;
		map[3][2] = 1;
		map[2][2] = 1;  // ���ڲ��Ի�������


		// �����ͼ
		System.out.println("------��ǰ��ͼ���------");
		for(int i = 0; i < map.length; i++) {
			for(int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}

		// ������·
		T t = new T();
		t.findWay(map, 1, 1);

		// �����ͼ����·������
		System.out.println("------·������------");
		for(int i = 0; i < map.length; i++) {
			for(int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}

	}
}

class T {
	// findWay�����������ҳ��Թ���·��������ҵ��ˣ��ͷ���true������ͷ���false
	// map�Ƕ�ά���飬��ʾ���ǵ��Թ���i��j��ʾ�����λ�ã���ʼ����λ��Ϊ1��1
	// ����Ҫʵ�ֵ��ǵݹ����·������Ҫ�涨map�����еĸ���ֵ�ĺ���
	// 0��ʾ���ϰ��1��ʾ�ϰ��2��ʾ�����ߵ�·��3��ʾ�߹���������һ����·
	// ��map[6][5] = 2ʱ����˵���ҵ�ͨ·�ˣ����Խ����ˣ�����͵ݹ������
	// ����������·�Ĳ��ԣ���->��->��->��   �������Ҳ�ͨ�������ұߣ��������ƣ����Բ�ͬ���ߵ�·������Ҳ��ͬ
	// ���ǿ����Ż��������ҵ���̵�·��
	public boolean findWay(int[][] map, int i, int j) {
		if(map[6][5] == 2) {  // ˵���Ѿ��ҵ�����
			return true;
		}
		else {
			if(map[i][j] == 0) {  // �����λ��Ϊ0ʱ��˵��������
				// ���Ǽٶ�������ͨ
				map[i][j] = 2;
				// ʹ����·���ԣ���->��->��->�󣩣���ȷ����λ���Ƿ���Ŀ�����ͨ
				if(findWay(map, i + 1, j)) {
					return true;
				}
				else if(findWay(map, i, j + 1)) {
					return true;
				}
				else if(findWay(map, i - 1, j)) {
					return true;
				}
				else if(findWay(map, i, j - 1)) {
					return true;
				}
				else {
					// ����������Ҷ��߲�ͨ�����ǽ�����·����Ϊ3
					map[i][j] = 3;
					return false;
				}
			}
			else {
				return false;
			}
		}
	}
}