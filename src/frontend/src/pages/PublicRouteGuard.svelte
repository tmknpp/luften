<script>
    import { Router, Route } from "svelte-routing";
    import LoginPage from './loginpage.svelte';
    // import { auth } from "../dataservices";
    // import HomePage from './Home.svelte';
    
</script>

    <Router>
        <Route  path="/login" component={LoginPage} />
    </Router>