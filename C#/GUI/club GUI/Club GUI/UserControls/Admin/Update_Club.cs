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
    public partial class Update_Club : UserControl
    {
        // A global Variable that will hold the name of the row to be changed
        string ClubName;
        public Update_Club()
        {
            InitializeComponent();
        }

        // Display Date
        private void Update_Club_Load(object sender, EventArgs e)
        {
            lbDate.Text = "(" + DateTime.UtcNow.ToString("MM-dd-yyyy") + ")";
        }

        // Displays a give category into the combobox
        private void showcat(string cat_name)
        {
            // Clear the comboBox
            cmbClub.Items.Clear();

            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            con.SqlQuery("SELECT * FROM Clubs WHERE Cat=@cat_name");
            con.cmd.Parameters.AddWithValue("@cat_name", cat_name);

            foreach (DataRow dr in con.QueryEx().Rows)
            {
                cmbClub.Items.Add(dr[0].ToString());
            }
        }

        /*********************************************Radio Buttons********************************************/

        private void Art_CheckedChanged(object sender, EventArgs e)
        {
            showcat("ArtOrganization");
        }

        private void Academic_CheckedChanged(object sender, EventArgs e)
        {
            showcat("Academic");
        }

        private void Sport_CheckedChanged(object sender, EventArgs e)
        {
            showcat("Sport");
        }

        /*****************************************ComboBox***************************/
        private void cmbClub_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            // Query table
            con.SqlQuery("SELECT * FROM Clubs WHERE Clubname=@club_name");
            con.cmd.Parameters.AddWithValue("@club_name", cmbClub.SelectedItem);

            // Display the data in the input fields
            foreach (DataRow dr in con.QueryEx().Rows)
            {
                // set club name
                ClubName = dr["ClubName"].ToString();
                tbClubName.Text = dr["ClubName"].ToString();

                tbCat.Text = dr["cat"].ToString();

                tbPresident.Text = dr["President"].ToString();

                tbVice.Text = dr["Vice"].ToString();

                rtbDes.Text = dr["Description"].ToString();
            }

            con.close();
        }

        // Clears every Field
        private void Clear_Fields()
        {
            tbClubName.Text = "";

            tbCat.Text = "";

            tbPresident.Text = "";

            tbVice.Text = "";

            rtbDes.Text = "";
        }
        // When update is clicked update the database
        private void Update_Click(object sender, EventArgs e)
        {
            // Check for empty fields
            if (tbClubName.Text == "" || tbCat.Text == "" || tbPresident.Text == "" || tbVice.Text == "" || rtbDes.Text == "")
            {
                MessageBox.Show("Fill all of the input fields", "Error");
            }
            else 
            {
                SqlDBConnect con = new SqlDBConnect();

                con.SqlQuery("UPDATE Clubs SET " +
                    "ClubName=@name, cat=@cat, RegDate=@regdate, President=@prez, Vice=@vice, Description=@des, LastUpdated=@lu" +
                    " WHERE ClubName=@clubname;");

                con.cmd.Parameters.AddWithValue("@clubname", ClubName);

                con.cmd.Parameters.AddWithValue("@name", tbClubName.Text);
                con.cmd.Parameters.AddWithValue("@cat", tbCat.Text);
                con.cmd.Parameters.AddWithValue("@regdate", DateTime.UtcNow.ToString("MM-dd-yyyy"));
                con.cmd.Parameters.AddWithValue("@prez", tbPresident.Text);
                con.cmd.Parameters.AddWithValue("@vice", tbVice.Text);
                con.cmd.Parameters.AddWithValue("@des", rtbDes.Text);
                con.cmd.Parameters.AddWithValue("@lu", DateTime.UtcNow.ToString());

                con.NonQueryEx();

                con.con.Close();

                MessageBox.Show("Club Updated Sucessfully", "Sucess");
                Clear_Fields();
            }
        }
    }
}
