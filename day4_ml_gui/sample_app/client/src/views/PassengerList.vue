<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        md12
      >
        <material-card
          :color="color"
          title="List of Passengers"
          text="You can see if the passenger survived or not"
        >
          <v-data-table
            v-if="!loading"
            :headers="headers"
            :items="items"
            hide-actions
          >
            <template
              slot="headerCell"
              slot-scope="{ header }"
            >
              <span
                class="subheading font-weight-light text-success text--darken-3"
                v-text="header.text"
              />
            </template>

            <template
              slot="items"
              slot-scope="{ item }"
            >
              <td>{{ item.first_name }}</td>
              <td>{{ item.last_name }}</td>
              <td>{{ sexMap[item.sex] }}</td>
              <td class="text-xs-right">{{ item.age }}</td>
              <td class="text-xs-right">{{ item.family_size }}</td>

              <td>{{ embarkedMap[item.embarked] }}</td>
              <td class="text-xs-right">{{ item.pclass }}</td>
              <td class="text-xs-right">{{ item.fare }}</td>
              <td :class="survivedMap[item.survived].class">{{ survivedMap[item.survived].text }}</td>

            </template>
          </v-data-table>

          <v-progress-linear
            v-if="loading"
            :size="50"
            :color="color"
            indeterminate
          />

        </material-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import {
  mapState
} from 'vuex'

export default {
  data: () => ({
    loading: true,
    headers: [
      {
        sortable: true,
        text: 'Fist Name',
        value: 'first_name'
      },
      {
        sortable: true,
        text: 'Last Name',
        value: 'last_name'
      },
      {
        sortable: true,
        text: 'Sex',
        value: 'sex'
      },
      {
        sortable: true,
        text: 'Age',
        value: 'age'
      },
      {
        sortable: true,
        text: 'Family Size',
        value: 'family_size'
      },
      {
        sortable: true,
        text: 'Embarked',
        value: 'embarked'
      },
      {
        sortable: true,
        text: 'Ticket Class',
        value: 'pclass'
      },
      {
        sortable: true,
        text: 'Fare',
        value: 'fare'
      },
      {
        sortable: true,
        text: 'Survived',
        value: 'survived'
      }
    ],
    sexMap: {
      0: 'Famale',
      1: 'Male'
    },
    embarkedMap: {
      0: 'Southampton',
      1: 'Cherbourg',
      2: 'Queenstown'
    },
    survivedMap: {
      0: {
        text: 'DEAD',
        class: 'text-danger'
      },
      1: {
        text: 'ALIVE',
        class: 'text-info'
      }

    },
    items: []
  }),
  computed: {
    ...mapState('app', ['image', 'color'])
  },
  mounted () {
    this.loadPassengers()
  },
  methods: {
    loadPassengers () {
      this.loading = true
      this.$axios.get('http://localhost:5000/api/passenger')
        .then(response => {
          this.items = response.data.passengers
          this.loading = false
        })
        .catch(() => {
          this.snackbar = {
            visible: true,
            color: 'negative',
            icon: 'mdi-alert',
            text: 'Failed to load'
          }
        })
    }
  }
}
</script>
