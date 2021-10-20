import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.lang.reflect.Type;
import java.util.function.Function;

public class AddDialog extends JDialog implements ActionListener {
 private JTextField itemNameTF;
 private JLabel itemLabel;
 private JTextField amtPurchaseTF;
 private JLabel amtPurchaseLabel;
 private JTextField priceTF;
 private JLabel priceLabel;
 private JButton oKB;

    public  AddDialog(){
        setTitle("Add Item");

        setLayout(new GridBagLayout());
        buildDialog();
        setSize(400,400);
        setResizable(false);
        setVisible(true);
    }
    private void buildDialog()
    {
        GridBagConstraints gc = new GridBagConstraints();
        gc.insets = new Insets(4,4,4,4);

        itemNameTF = new JTextField("Item Name",15);
        itemNameTF.setFont(new Font("New Times Roman" , Font.ITALIC, 12));
        amtPurchaseTF = new JTextField("Amount Purchased",10);

        oKB = new JButton("Ok");
        oKB.addActionListener(this);
        this.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                super.mouseClicked(e);
                    if(e.getSource() == itemNameTF) {
                        itemNameTF.setFont(new Font("New Times Roman", Font.PLAIN, 12));
                        itemNameTF.setText("");

                    }
                    else if(e.getSource() == amtPurchaseTF){

                        System.out.println("it works.");
                    }
                    //A
            }
        });









        gc.gridx = 0;
        gc.gridy = 0;
        add(itemNameTF,gc);



        gc.gridx = 0;
        gc.gridy = 1;
        add(amtPurchaseTF,gc);

        gc.gridx = 4;
        gc.gridy = 4;
        add(oKB,gc);

    }





    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == oKB) {

            Object[]options = {"Yes", "no"};
            String itemStr = itemNameTF.getText();
           int n = JOptionPane.showOptionDialog(this, "Are you sure you want to add " +itemStr+"?", "Confirm", JOptionPane.YES_NO_CANCEL_OPTION, JOptionPane.QUESTION_MESSAGE, null, options,options[1]);
            if(n == 0) {
                System.out.println(itemStr + " has been added.");
                dispose();
            }
            else{
                System.out.println(itemStr +" was not added.");
            }


        }
    }
}


