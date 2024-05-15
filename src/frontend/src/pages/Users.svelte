<script>
    import { use } from "marked";
    import { listPupils, getPupil } from "../dataservices";
    import { selectedPupil} from "../stores/selectedPupil";


    import PupilInteraction from "../sveltelib/components/pupil/pupilInteraction.svelte";
    import PupilInteractions from "../sveltelib/components/pupil/pupilInteractions.svelte";
    $: users = $listPupils
    let role = "user"
    let currentUser= "";

</script>


{#if role == "admin"}
    <div class="container-admin"> 


        <div class="containervert-sidebar">
            {#each users as user}

            <label> 
                <input type="radio" bind:group={$selectedPupil} value={user} />
                    {user[1]}
            </label>

            {/each}
        </div>

        <div class="containervert">
            <div class="pupil-interactions">
                <PupilInteractions></PupilInteractions>
            </div>
            <div class="pupil-interaction">
            <PupilInteraction></PupilInteraction>
            </div>
        </div>
    </div>
{/if}

{#if role == "user"}
    <div class="container-user">
        <p>Testing user view</p>
        <div class="containervert">
            <div class="pupil-interactions">
                <PupilInteractions></PupilInteractions>
            </div>
            <div class="pupil-interaction">
            <PupilInteraction></PupilInteraction>
            </div>
        </div>
    </div>
{/if}

<style>
    .container-admin {
      display: flex;
      flex-direction: row; /* Horizontal layout by default */
      width: 1500px;
    }

    .container-user {
      display: flex;
      flex-direction: row; /* Horizontal layout by default */
      width: 1500px;
    }

    .containervert-sidebar {
      display: flex;
      flex-direction: column; /* Horizontal layout by default */
      width: 10%;
    }

    .containervert {
      display: flex;
      height: 100vh;
      flex-direction: row; /* Horizontal layout by default */
      overflow: hidden; /* Ensures no overflow from child components */
      width: 87%;
    }

 /* Specific to the component containing the messages */
    .pupil-interactions {
    
        flex: 1; /* Allows this component to grow and fill the space but not beyond */
        width: 66%;
    }

    /* Container for the input area should not grow */
    .pupil-interaction {
        width: 33%;
        flex: 0 1 auto; /* Does not grow, but can shrink to fit content */
    }

</style>