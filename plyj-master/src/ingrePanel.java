import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ingrePanel extends JPanel implements ActionListener {

    private JTabbedPane tabbedPane;
    private JToolBar ingreToolBar;
    private JTextField ingreSearchTF;
    private JButton ingreSearchB;
    private JButton ingreAddB;
    private JButton ingreUpdateB;
    private JButton ingreRemoveB;
    private JButton ingreListAllB;

    public ingrePanel(){


        buildIngrePanel();

    }


private void buildIngrePanel(){


    ingreToolBar =new JToolBar();
    ingreToolBar.setFloatable(false);
    ingreSearchB =new JButton("Search");
    ingreSearchTF =new JTextField(10);

    ingreAddB =new JButton("Add");

    ingreUpdateB =new JButton("Update");

    ingreRemoveB = new JButton("Remove");

    ingreListAllB =new JButton("List All");

    //The following code builds toolbar;
    {
        ingreToolBar.add(ingreSearchTF);

        ingreToolBar.add(ingreSearchB);
        ingreToolBar.add(ingreAddB);
        ingreToolBar.add(ingreUpdateB);
        ingreToolBar.add(ingreRemoveB);
        ingreToolBar.addSeparator();
        ingreToolBar.add(ingreListAllB);
    }

    //add the listener to the  Buttons
    {

        ingreSearchB.addActionListener(this);
        ingreAddB.addActionListener(this);
        ingreUpdateB.addActionListener(this);
        ingreRemoveB.addActionListener(this);
        ingreListAllB.addActionListener(this);


    }
      add(ingreToolBar);

      ingreSearchTF.setBounds(250,250,50,25);





}


    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == ingreSearchB) {
            System.out.println(ingreSearchTF.getText());
        }
        else if(e.getSource() == ingreAddB)
        {
            new AddDialog();
            System.out.println("Add");
        }
        else if(e.getSource() == ingreUpdateB)
        {
            System.out.println("Update");

        }
        else if(e.getSource() == ingreRemoveB)
        {
            System.out.println("Remove");
        }
        else if(e.getSource() == ingreListAllB){

            System.out.println("list all");

        }
    }

}
