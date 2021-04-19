import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main_사회망서비스 {

	private static int N;
	private static boolean[] visited;
	private static int[][] dp;
	public static LinkedList<Integer>[] friendList;

	public static void main(String[] args) throws Exception {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			N = Integer.parseInt(br.readLine());
	      
	      
			StringTokenizer st;
			visited = new boolean[N+1];
			dp = new int[N+1][2];
	      
			friendList = new LinkedList[N+1];
			// 정점 N개의 인접 리스트 생성 
			for (int i = 1; i <= N; i++) {
				friendList[i] = new LinkedList<Integer>();
			}
			for (int i = 0; i < N-1; i++) {
				st = new StringTokenizer(br.readLine());
	    	  
				int u = Integer.parseInt(st.nextToken());
				int v = Integer.parseInt(st.nextToken());
				
				friendList[u].add(v);
				friendList[v].add(u);
			
			}
	      
			dfs(1);
			
			int answer = Math.min(dp[1][0], dp[1][1]);
			System.out.println(answer);
	}
	
	public static void dfs(int idx) {
		visited[idx] = true;
		dp[idx][0] = 0;
		dp[idx][1] = 1;
		
		for (int i = 0; i < friendList[idx].size(); i++) {
			int next = friendList[idx].get(i);
			
			if(visited[next]) continue;
			
			dfs(next);
			dp[idx][0] += dp[next][1]; //  내가 얼리가 아니면 내 친구들은 다 얼리~~
			dp[idx][1] += Math.min(dp[next][0], dp[next][1]); // 내가 얼리라면 친구는 얼리여도 되고 아니어도 되고
		}
		
	}

}
