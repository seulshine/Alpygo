import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;
public class Main_1991트리순회 {

	private static int N;
	private static HashMap<Character, Node> map;

	static class Node {
		char alpha;
		char left;
		char right;
		public Node(char alpha, char left, char right) {
			super();
			this.alpha = alpha;
			this.left = left;
			this.right = right;
		}

		
		
	}
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());

		map = new HashMap<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");

			char alpha = st.nextToken().charAt(0);
			char left = st.nextToken().charAt(0);
			char right = st.nextToken().charAt(0);
			
			
			map.put(alpha, new Node(alpha, left, right));
			
		}
		
		preOrder('A');
		System.out.println();
		inOrder('A');
		System.out.println();
		postOrder('A');
	}
	
	
	public static void preOrder(char now) {
		System.out.print(now);
		Node temp = map.get(now);
		
		if(temp.left != '.') {
			preOrder(temp.left);
		}
		if(temp.right != '.') {
			preOrder(temp.right);
		}
		
	}
	
	public static void inOrder(char now) {
		Node temp = map.get(now);
		
		if(temp.left != '.') {
			inOrder(temp.left);
		}
		
		System.out.print(now);
		
		if(temp.right != '.') {
			inOrder(temp.right);
		}
		
	}
	
	public static void postOrder(char now) {

		Node temp = map.get(now);
		
		if(temp.left != '.') {
			postOrder(temp.left);
		}
		if(temp.right != '.') {
			postOrder(temp.right);
		}
		
		System.out.print(now);
		
	}

}
