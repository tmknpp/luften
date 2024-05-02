<script>

    
    import AssistantPage from "../pages/administration/Assistant.svelte"
    import UsersPage from "../pages/administration/Users.svelte"
    import { Router, Route, Link } from "svelte-routing";


    let tabs2 = [
        {name:'Assistant', route: 'assistant', component: AssistantPage},
       {name:'Users', route: 'users', component: UsersPage}
  ]
</script>

The core philosopy of this project is that, to reduce the cognitive load of programming, it is sufficient to solve all 
data related issues within the openai beta framework. The openai beta framework provides extensible assistant, thread 
and message related apis. This project, through the assistance of a helper framework (betaassi), illustrates how to reduce
the cognitive load of programming.

<Router>



    <div class="container">
        <div class="sidebar">
            <ul>
                <li><Link to="users">Users</Link></li>
            </ul>
            <ul>
                <li><Link to="assistant">Assistant</Link></li>
            </ul>

        </div>

        <div class="main-content">

            <Route path="users" component={UsersPage} />
            <Route path="assistant" component={AssistantPage} />
        </div>
    </div>
</Router>







<style>
    .container {
      display: flex;
      flex-direction: row; /* Horizontal layout by default */
      width: 100%;
    }
  
    .sidebar {
      width: 10%;
      padding: 10px;
    }
  


    .sidebar ul {
    list-style-type: none; /* Removes bullet points */
    padding-left: 0; /* Removes padding on the left */
    margin: 0; /* Removes default margin */
  }

  .sidebar li {
    padding: 8px; /* Adds padding to each list item for spacing */
    margin-bottom: 5px; /* Adds space between list items */
    border-bottom: 1px solid #ccc; /* Optional: adds a subtle line between items */
  }
    .main-content {
      width: 90%;
      padding: 10px;
    }
  
    /* Responsive adjustments */
    @media (max-width: 768px) {
      .container {
        flex-direction: column; /* Stack vertically on small screens */
      }
      .sidebar, .main-content {
        width: 100%; /* Both take full width on small screens */
      }
    }
  </style>
  


