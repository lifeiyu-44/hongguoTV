import java.io.File;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.nio.charset.StandardCharsets;

public class RenameProbe {
    public static void main(String[] args) throws Exception {
        File folder = new File(args[0]);
        folder.mkdirs();
        File partial = new File(folder, "probe.apk.part");
        File destination = new File(folder, "probe.apk");
        try {
            try (FileOutputStream out = new FileOutputStream(destination)) {
                out.write("previous".getBytes(StandardCharsets.UTF_8));
            }
            try (FileOutputStream out = new FileOutputStream(partial)) {
                out.write("verified-new-apk".getBytes(StandardCharsets.UTF_8));
                out.getFD().sync();
            }
            boolean renamed = partial.renameTo(destination);
            byte[] data = new byte[(int) destination.length()];
            try (FileInputStream input = new FileInputStream(destination)) {
                if (input.read(data) != data.length) throw new AssertionError("short read");
            }
            String content = new String(data, StandardCharsets.UTF_8);
            System.out.println("renamed=" + renamed + "; content=" + content);
            if (args.length > 1 && (!renamed || !content.equals("verified-new-apk"))) {
                throw new AssertionError("replacement failed");
            }
        } finally {
            partial.delete(); destination.delete(); folder.delete();
        }
    }
}
