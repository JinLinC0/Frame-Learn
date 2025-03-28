public class MiGong {
	public static void main(String[] args) {
		// 初始化迷宫的形状
		int [][] map = new int [8][7];

		// 将最上面一行和最下面一行，全部设置为1
		for(int i = 0; i < 7; i++) {
			map[0][i] = 1;   // 最上面一行
			map[7][i] = 1;   // 最下面一行
		}

		// 将最第一列和最后一列，全部设置为1
		for(int i = 0; i < 8; i++) {
			map[i][0] = 1;   // 最左边一列
			map[i][6] = 1;   // 最右边一列
		}

		// 将[3][1]和[3][2]和[2][2]位置设置为1
		map[3][1] = 1;
		map[3][2] = 1;
		map[2][2] = 1;  // 用于测试回溯现象


		// 输出地图
		System.out.println("------当前地图情况------");
		for(int i = 0; i < map.length; i++) {
			for(int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}

		// 老鼠找路
		T t = new T();
		t.findWay(map, 1, 1);

		// 输出地图，找路后的情况
		System.out.println("------路后的情况------");
		for(int i = 0; i < map.length; i++) {
			for(int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}

	}
}

class T {
	// findWay方法：用于找出迷宫的路径，如果找到了，就返回true，否则就返回false
	// map是二维数组，表示我们的迷宫；i和j表示老鼠的位置，初始化的位置为1，1
	// 我们要实现的是递归的找路，我们要规定map数组中的各个值的含义
	// 0表示无障碍物；1表示障碍物；2表示可以走的路；3表示走过，但是是一条死路
	// 当map[6][5] = 2时，就说明找到通路了，可以结束了，否则就递归继续找
	// 定义老鼠找路的策略：下->右->上->左   （下面找不通，再找右边，依次类推）策略不同，走的路径长度也不同
	// 我们可以优化策略来找到最短的路径
	public boolean findWay(int[][] map, int i, int j) {
		if(map[6][5] == 2) {  // 说明已经找到出口
			return true;
		}
		else {
			if(map[i][j] == 0) {  // 当这个位置为0时，说明可以走
				// 我们假定可以走通
				map[i][j] = 2;
				// 使用找路策略（下->右->上->左），来确定该位置是否真的可以走通
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
					// 如果上下左右都走不通，我们将这条路设置为3
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