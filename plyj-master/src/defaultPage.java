import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class defaultPage  extends JFrame {
        private JPanel recepPanel;
        private JPanel formPanel;
        private JTabbedPane tabbedPane;

   private JTabbedPane ingredientsTab;

    public defaultPage()
    {
        tabbedPane = new JTabbedPane();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        recepPanel = new JPanel();
        tabbedPane.add("Ingredients", new ingrePanel());
        tabbedPane.add("Recipes", recepPanel);
        tabbedPane.add("Form", formPanel);

        add(tabbedPane);

        setSize(500, 500);
        setVisible(true);
    }



}
