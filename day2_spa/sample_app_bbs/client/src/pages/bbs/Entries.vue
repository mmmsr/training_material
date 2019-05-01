<template>
  <q-page
    class="docs-input row justify-center"
    padding
  >
    <div style="width: 500px; max-width: 90vw;">
      <h6 style="color: #027be3;">
        BBS Posts
      </h6>

      <div
        v-for="entry in entries"
        :key="entry.id"
      >
        <q-card
          class="my-card"
        >
          <q-card-section>
            <div class="text-h6">
              {{ entry.title }}
            </div>
            <div class="text-subtitle2">
              {{ entry.posted_by }}
            </div>
          </q-card-section>
          <q-card-section>
            {{ entry.created_at }}
          </q-card-section>
        </q-card>
        <br>
      </div>
    </div>

    <q-page-sticky
      position="bottom-right"
      :offset="[18, 18]"
    >
      <q-btn
        fab
        icon="add"
        color="primary"
        to="/bbs/new-entry"
      />
    </q-page-sticky>
  </q-page>
</template>

<style></style>

<script>
export default {
  name: "Entries",
  data() {
    return {
      entries: []
    }
  },
  methods: {
    loadEntries() {
      this.$axios.get("http://localhost:5000/api/entry")
        .then(response => {
          this.entries = response.data.entries
        })
        .catch(() => {
          this.$q.notify({
            color: 'negative',
            position: 'top',
            message: 'Loading failed',
            icon: 'report_problem'
          })
        })
    }
  },
  created(){
    this.loadEntries()
  }
}
</script>
