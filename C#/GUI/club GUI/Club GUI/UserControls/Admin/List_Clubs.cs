using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Club_GUI
{
    public partial class List_Clubs : UserControl
    {
        public List_Clubs()
        {
            InitializeComponent();
        }

        // Display Date and Time
        private void List_Clubs_Load(object sender, EventArgs e)
        {
            // Open connection
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();



            /************************Get Categories*******************************************/
            con.SqlQuery("SELECT DISTINCT cat FROM Clubs ORDER BY cat;");
            DataTable cat_table = con.QueryEx();

            int size = cat_table.Rows.Count;
            string[] cat = new string[size];

            // polpulate the array
            int count = 0;
            foreach (DataRow dr in cat_table.Rows)
            {
                cat[count] = dr["cat"].ToString();
                count++;
            }

            /*********************************** Display Details****************************/
            string[] state = { "active", "inactive" };
            for (int j = 0; j < state.Length; j++)
            {
                rtbList.Text += state[j] + "\n\n";
                for (int i = 0; i < cat.Length; i++)
                {
                    //Query
                    con.SqlQuery("SELECT * FROM Clubs WHERE cat=@cat_name AND State=@state ORDER BY ClubName;");

                    // Add dynamic parameters
                    con.cmd.Parameters.AddWithValue("@cat_name", cat[i]);
                    con.cmd.Parameters.AddWithValue("@state", state[j]);

                    // Execute
                    DataTable table = con.QueryEx();


                    // Display cat
                    rtbList.Text += cat[i] + "\n\n";

                    // Display row
                    foreach (DataRow dr in table.Rows)
                    {
                        string club_info = dr["ClubName"] + "(" + dr["RegDate"] + ")" +
                            "\n\nPresident: " + dr["President"] + "\nVice President: " + dr["Vice"] + "\n\n" +
                            "Last Updated: " + dr["LastUpdated"] + "\n" + dr["Description"] + "\n\n\n";

                        rtbList.Text += club_info;
                    }

                    rtbList.Text += "\n\n_______________________________________________________________________________________\n";
                }
                rtbList.Text += "**********************************************************************\n\n\n";
            }
            // Close Connection
            con.con.Close();
        }
    }
}
