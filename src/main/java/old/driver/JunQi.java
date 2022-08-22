package old.driver;

import java.io.File;
import java.net.URL;

/**
 * @author
 * @date 2022/8/22 16:47
 * Description:
 */
public class JunQi {



    public static void main(String[] args) {
        JunQi junqi = new JunQi();
        URL path = junqi.getClass().getClassLoader().getResource("game");
        File dir = new File(path.getPath());
        for (File file :dir.listFiles()) {
            String fileName = file.getName();
            String date = fileName.substring(0, 2) + "年" + fileName.substring(2, 4) + "月" + fileName.substring(4, 6) + "日" + fileName.substring(6, 8) + "时";
            String vs = fileName.substring(13, fileName.length() - 4);
            System.out.println(date + "  " + vs);
        }

    }
}
