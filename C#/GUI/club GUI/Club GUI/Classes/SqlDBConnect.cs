using System.Data.Sql;
using System.Data.SqlClient;
using System.Data;
using System.Security.AccessControl;

namespace Club_GUI.Classes
{
    public class SqlDBConnect
    {
        public SqlConnection con;

        public SqlCommand cmd;

        private SqlDataAdapter _da;
        private DataTable _dt;

        public SqlDBConnect()
        {
            // Connecion might differ
            con = new SqlConnection("Data Source=(LocalDB)\\MSSQLLocalDB;AttachDbFilename=\"C:\\USERS\\YAHYA SHERIF\\DESKTOP\\PROJECTS\\C#\\GUI\\CLUB GUI\\DATABASE\\CLUB_DATABASE.MDF\";Integrated Security=True;Connect Timeout=30");
            con.Open();
        }

        public void SqlQuery(string QueryText)
        {
            cmd = new SqlCommand(QueryText, con);
        }

        // For SELECT statements
        public DataTable QueryEx()
        {
            _dt = new DataTable();
            _da = new SqlDataAdapter(cmd);

            _da.Fill(_dt);

            return _dt;
        }

        // For INSERT, UPDATE, and DELETE statements
        public void NonQueryEx() 
        {
            cmd.ExecuteNonQuery();
        }

        public void close()
        {
            con.Close();
        }
    }
}
