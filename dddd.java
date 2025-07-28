import java.io.*;
import java.util.*;

public class dddd {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] grid = new int[N][N];

        for (int i = 0; i < N; i++) {
            String[] rowValues = br.readLine().split("#");
            for (int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(rowValues[j]);
            }
        }

        int maxMinMoney = -1;
        List<String> resultPositions = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int currentMin = Integer.MAX_VALUE;

                for (int rowOffset = -1; rowOffset <= 1; rowOffset++) {
                    for (int colOffset = -1; colOffset <= 1; colOffset++) {
                        int neighborRow = i + rowOffset;
                        int neighborCol = j + colOffset;

                        if (neighborRow >= 0 && neighborRow < N && neighborCol >= 0 && neighborCol < N) {
                            currentMin = Math.min(currentMin, grid[neighborRow][neighborCol]);
                        }
                    }
                }

                if (currentMin > maxMinMoney) {
                    maxMinMoney = currentMin;
                    resultPositions.clear();
                    resultPositions.add((i + 1) + "#" + (j + 1));
                } else if (currentMin == maxMinMoney) {
                    resultPositions.add((i + 1) + "#" + (j + 1));
                }
            }
        }

        for (String position : resultPositions) {
            System.out.println(position);
        }

        br.close();
    }
}