using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Club_GUI.Classes;

namespace Club_GUI
{
    public partial class Delete_Club : UserControl
    {
        public Delete_Club()
        {
            InitializeComponent();
        }

        // Displays a give category into the combobox
        private void showstate(string state)
        {
            // Clear the comboBox
            cmbClub.Items.Clear();

            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            con.SqlQuery("SELECT * FROM Clubs WHERE State=@state ORDER BY ClubName");
            con.cmd.Parameters.AddWithValue("@state", state);

            foreach (DataRow dr in con.QueryEx().Rows)
            {
                cmbClub.Items.Add(dr[0].ToString());
            }

            // Close Connection
            con.con.Close();
        }

        // when the user picks a club display it
        private void cmbClub_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            // Query table
            con.SqlQuery("SELECT * FROM Clubs WHERE Clubname=@club_name");
            con.cmd.Parameters.AddWithValue("@club_name", cmbClub.SelectedItem);

            DataTable table = con.QueryEx();

            dgvClub.DataSource = table;

            // Close Connection
            con.con.Close();
        }

        // When the user picks a cat display its clubs
        private void displaystate(string state)
        {
            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            con.SqlQuery("SELECT * FROM Clubs WHERE State=@state ORDER BY ClubName");
            con.cmd.Parameters.AddWithValue("@state", state);

            DataTable table = con.QueryEx();
            dgvClub.DataSource = table;

            // Close Connection
            con.con.Close();
        }

        /*********************************************Radio Buttons********************************************/

        private void Active_CheckedChanged(object sender, EventArgs e)
        {
            showstate("active");
            displaystate("active");
        }

        private void Inactive_CheckedChanged(object sender, EventArgs e)
        {
            showstate("inactive");
            displaystate("inactive");
        }

        // Set club to inactive
        private void Archive_Click(object sender, EventArgs e)
        {
            if (cmbClub.SelectedIndex > -1)
            {
                DialogResult result = MessageBox.Show("Are you sure that you want to archive to " + cmbClub.SelectedItem + "? ", "Confirmation", MessageBoxButtons.YesNo);

                if (result == System.Windows.Forms.DialogResult.Yes)
                {
                    // set connection
                    SqlDBConnect con = new SqlDBConnect();

                    // Query
                    con.SqlQuery("UPDATE Clubs SET State='inactive' WHERE ClubName=@name;");

                    con.cmd.Parameters.AddWithValue("@name", cmbClub.SelectedItem.ToString());

                    // Execute
                    con.NonQueryEx();

                    // close
                    con.close();

                    MessageBox.Show("Done successfully", "Success");
                }
            }
            else
            {
                MessageBox.Show("No item selected", "Error");
            }
        }

        // Deletes Club
        private void Delete_Click(object sender, EventArgs e)
        {
            if (cmbClub.SelectedIndex > -1)
            {
                DialogResult result = MessageBox.Show("Are you sure that you want to delete to " + cmbClub.SelectedItem + "? ", "Confirmation", MessageBoxButtons.YesNo);

                if (result == System.Windows.Forms.DialogResult.Yes)
                {
                    // set connection
                    SqlDBConnect con = new SqlDBConnect();

                    // Query
                    con.SqlQuery("DELETE FROM Clubs WHERE ClubName=@name;");

                    con.cmd.Parameters.AddWithValue("@name", cmbClub.SelectedItem.ToString());

                    // Execute
                    con.NonQueryEx();

                    // close
                    con.close();

                    MessageBox.Show("Done successfully", "Success");
                }
            }
            else
            {
                MessageBox.Show("No item selected", "Error");
            }
        }

        // Set club to active
        private void Unarchive_Click(object sender, EventArgs e)
        {
            if (cmbClub.SelectedIndex > -1)
            {
                DialogResult result = MessageBox.Show("Are you sure that you want to unarchive to " + cmbClub.SelectedItem + "? ", "Confirmation", MessageBoxButtons.YesNo);

                if (result == System.Windows.Forms.DialogResult.Yes)
                {
                    // set connection
                    SqlDBConnect con = new SqlDBConnect();

                    // Query
                    con.SqlQuery("UPDATE Clubs SET State='active' WHERE ClubName=@name;");

                    con.cmd.Parameters.AddWithValue("@name", cmbClub.SelectedItem.ToString());

                    // Execute
                    con.NonQueryEx();

                    // close
                    con.close();

                    MessageBox.Show("Done successfully", "Success");
                }
            }
            else
            {
                MessageBox.Show("No item selected", "Error");
            }
        }
    }
}
