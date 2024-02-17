package org.Figuras;
import javax.swing.JOptionPane;

public class Main extends javax.swing.JFrame {
    Cuadrado cuadrado;
    Triangulo triangulo;
    Rectangulo rectangulo;
    Poligono poligono;
    public Main() {
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        Calcular = new javax.swing.JButton();
        AlturaIN = new javax.swing.JTextField();
        Basetxt = new javax.swing.JLabel();
        figIN = new javax.swing.JLabel();
        BaseIN = new javax.swing.JTextField();
        Areatxt = new javax.swing.JLabel();
        AreaOUT = new javax.swing.JTextField();
        listFig = new javax.swing.JComboBox<>();
        Alturatxt1 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Figuras Geometricas");
        setBackground(javax.swing.UIManager.getDefaults().getColor("Actions.Blue"));

        Calcular.setText("Calcular");
        Calcular.setToolTipText("");
        Calcular.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                CalcularActionPerformed(evt);
            }
        });

        AlturaIN.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        Basetxt.setText("Lado / Base / Perimetro : ");

        figIN.setText("Seleccione una figura:");

        BaseIN.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        Areatxt.setText("Area:");

        AreaOUT.setEditable(false);
        AreaOUT.setBackground(new java.awt.Color(255, 255, 255));
        AreaOUT.setHorizontalAlignment(javax.swing.JTextField.CENTER);
        AreaOUT.setAutoscrolls(false);

        listFig.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Cuadrado", "Triangulo", "Rectangulo", "Poligono" }));

        Alturatxt1.setText("Lado / Altura / Apotema :");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(Basetxt)
                        .addGap(18, 18, 18))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(16, 16, 16)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(Areatxt)
                            .addComponent(Alturatxt1))
                        .addGap(16, 16, 16)))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addComponent(BaseIN, javax.swing.GroupLayout.DEFAULT_SIZE, 118, Short.MAX_VALUE)
                        .addComponent(AlturaIN))
                    .addComponent(AreaOUT, javax.swing.GroupLayout.PREFERRED_SIZE, 118, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(29, 29, 29)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(listFig, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(figIN))
                .addGap(29, 29, 29))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(Calcular)
                .addGap(194, 194, 194))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(26, 26, 26)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(Basetxt)
                            .addComponent(BaseIN, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(Alturatxt1)
                            .addComponent(AlturaIN, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addComponent(Areatxt))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(46, 46, 46)
                        .addComponent(figIN)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(listFig, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(16, 16, 16)
                        .addComponent(AreaOUT, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(18, 18, 18)
                .addComponent(Calcular)
                .addContainerGap(20, Short.MAX_VALUE))
        );

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void CalcularActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_CalcularActionPerformed
        //Verificara que los datos INPUT sean numeros
        try{
            double base_= Double.parseDouble(BaseIN.getText());
            double altura_ = Double.parseDouble(AlturaIN.getText());  
        
        if (base_>=0 && altura_>=0)
        {
            String figuraUI = listFig.getSelectedItem().toString();
            switch (figuraUI)
            {
                case "Cuadrado":
                    cuadrado = new Cuadrado();
                    cuadrado.setLado1(base_);
                    cuadrado.setLado2(altura_);
                    cuadrado.calcularArea();
                    AreaOUT.setText(cuadrado.getArea().toString());
                    break;

                case "Triangulo":

                    triangulo = new Triangulo();
                    triangulo.setBase(base_);
                    triangulo.setAltura(altura_);
                    triangulo.calcularArea();
                    AreaOUT.setText(triangulo.getArea().toString());
                break;
                case "Rectangulo":

                    rectangulo = new Rectangulo();
                    rectangulo.setBase(base_);
                    rectangulo.setAltura(altura_);
                    rectangulo.calcularArea();
                    AreaOUT.setText(rectangulo.getArea().toString());
                break;
                case "Poligono":

                    poligono = new Poligono();
                    poligono.setPerimetro(base_);
                    poligono.setApotema(altura_);
                    poligono.calcularArea();
                    AreaOUT.setText(poligono.getArea().toString());
                break;
            }
        }else{
            // Mostrar el MessageBox
            JOptionPane.showMessageDialog(null, "Valor no Aceptado", "Error", JOptionPane.INFORMATION_MESSAGE);
            AreaOUT.setText("");
        }
        }catch(NumberFormatException e){
            JOptionPane.showMessageDialog(null, "Valor no Aceptado", "Error", JOptionPane.INFORMATION_MESSAGE);
            AreaOUT.setText("");
        }
    }//GEN-LAST:event_CalcularActionPerformed

   
    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                
                new Main().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JTextField AlturaIN;
    private javax.swing.JLabel Alturatxt1;
    private javax.swing.JTextField AreaOUT;
    private javax.swing.JLabel Areatxt;
    private javax.swing.JTextField BaseIN;
    private javax.swing.JLabel Basetxt;
    private javax.swing.JButton Calcular;
    private javax.swing.JLabel figIN;
    private javax.swing.JComboBox<String> listFig;
    // End of variables declaration//GEN-END:variables
}
