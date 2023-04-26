/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package imagedisplay;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
/**
 *
 * @author khalid
 */
public class ImageDisplay implements ActionListener {
    JFrame frame;
    JButton button1, button2;
    JLabel label;
    ImageIcon image1, image2;

    public ImageDisplay() {
        frame = new JFrame("Image Display");
        button1 = new JButton("Solved puzzle");
        button2 = new JButton("Unsolved puzzle");
        label = new JLabel();

        image1 = new ImageIcon("image2.jpg");
        image2 = new ImageIcon("image1.jpg");

        button1.addActionListener(this);
        button2.addActionListener(this);

        JPanel panel = new JPanel();
        panel.add(button1);
        panel.add(button2);
        frame.add(panel, BorderLayout.NORTH);
        frame.add(label, BorderLayout.CENTER);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == button1) {
            label.setIcon(image1);
        } else if (e.getSource() == button2) {
            label.setIcon(image2);
        }
    }

    public static void main(String[] args) {
        new ImageDisplay();
    }
}