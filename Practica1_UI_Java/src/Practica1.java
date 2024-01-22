import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Practica1 extends JFrame implements ActionListener {
    private JLabel IbNombre;
    private JTextField txNombre;
    private JButton btVer;

    public Practica1(){
        this.setBounds(0,0,350,120);
        this.setLayout(null);

        IbNombre =new JLabel(); //Creamos objeto, ventana principal
        IbNombre.setBounds(10,10,150,30);
        IbNombre.setName("IbNombre");
        IbNombre.setText("Ingrese nombre: ");
        IbNombre.setVisible(true);
        this.add(IbNombre);

        txNombre = new JTextField();//Caja de texto para nuestra entrada
        txNombre.setBounds(115,10,100,30);
        txNombre.setName("txNombre");
        txNombre.setVisible(true);
        txNombre.setText(" ");
        this.add(txNombre);

        btVer = new JButton();//Boton de ver que ejecutara una funcion
        btVer.setBounds(215,10,70,30);
        btVer.setName("btVer");
        btVer.setText("Ver");
        btVer.setVisible(true);
        btVer.addActionListener(this);
        this.add(btVer);

        this.setVisible(true);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Cerrado automatico de la ventana
    }

    public void actionPerformed(ActionEvent e){
        if(e.getSource() == btVer){
            JOptionPane.showMessageDialog(this,"Hola: "+ txNombre.getText());//Abrira una ventana emergente con este texto
        }
    }
    public static void main(String[] args) {  //METODO PRINCIPAL DEL CODIGO INTERFAZ
        Practica1 ob = new Practica1();
        ob.setVisible(true);
    }
}
