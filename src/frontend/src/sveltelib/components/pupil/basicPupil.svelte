<script>

    import { selectedPupil} from "../../../stores/selectedPupil";
    import { listPupils, getPupil } from "../../../dataservices";

    let pupilDetails = null

    $: if ($selectedPupil) {
        getPupil($selectedPupil[0]).then(details => { pupilDetails = details}).catch(error => {console.log(error)})
    }


    function toDateTime(secs) {
        var t = new Date(0)
        t.setSeconds(secs)
        return t
    }


</script>





{#if pupilDetails}

            {pupilDetails.pupil_id}             Created At: {toDateTime(pupilDetails.created_at)}


{/if}


<style>
    .container {
        display: flex;
        flex-direction: row; /* Horizontal layout by default */

        gap: 20px;
    }
</style>