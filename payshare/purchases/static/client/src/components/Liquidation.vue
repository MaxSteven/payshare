<template>

<div>
  <v-card class="my-2">
    <v-card-text class="px-2 pt-2 pb-0">
      <v-icon color="grey lighten-3"
              class="transfer-delete-btn"
              @click="softdelete(liquidation.name, liquidation)">
        close
      </v-icon>
      <v-layout row
                align-center>
        <v-layout v-bind="layout"
                  align-center
                  justify-center
                  class="no-grow mr-2 mb-2">
          <div v-if="creditor.avatar"
               class="avatar">
            <img :src="creditor.avatar"
                 class="avatar">
          </div>
          <v-icon class="pa-0 liquidation-arrow grey--text"
                  v-if="$vuetify.breakpoint.smAndUp">
            arrow_right
          </v-icon>
          <v-icon class="pa-0 liquidation-arrow grey--text"
                  v-else>
            arrow_drop_down
          </v-icon>
          <div v-if="debtor.avatar"
               class="avatar">
            <img :src="debtor.avatar"
                 class="avatar">
          </div>
        </v-layout>
        <v-layout v-bind="layout"
                  align-baseline
                  fill-height>
          <div class="text">
            <div class="description">
              <strong :class="{'primary--text': isCreditor}">
                {{ creditor.username }}
              </strong>
              {{ $t('gaveMoneyTo') }}
              <strong :class="{'primary--text': isDebtor}">
                {{ debtor.username }}
              </strong>
              {{ $t('for') }} <br>
            </div>
            <div class="name">
              {{ liquidation.name }}
            </div>
          </div>
          <v-spacer></v-spacer>
          <v-layout column
                    :style="{'width': $vuetify.breakpoint.xsOnly ? '100%' : 'initial'}"
                    fill-height>
            <div class="text-xs-right clickable"
                 @click="onCreatedDateClicked()">
              {{ showAgoInsteadOfDate ? createdDateAgo : createdDateFormatted }}
            </div>
            <div class="pl-5 amount"
                 :class="{'secondary--text': !isCreditor && !isDebtor,
                          'red--text': isDebtor,
                          'green--text': isCreditor}">
              {{ amount }}
              <span class="currency">
                {{ collective.currency_symbol }}
              </span>
            </div>
          </v-layout>
        </v-layout>
      </v-layout>
    </v-card-text>
  </v-card>
</div>

</template>

<script>

import createdDate from '@/mixins/createdDate'
import selectedMember from '@/mixins/selectedMember'
import softdelete from '@/mixins/softdelete'

export default {
  mixins: [
    createdDate,
    selectedMember,
    softdelete,
  ],
  name: 'liquidation',
  props: {
    'liquidation': {
      type: Object,
      required: true,
    },
  },
  computed: {
    transfer() {
      return this.liquidation
    },
    layout() {
      if (this.$vuetify.breakpoint.xsOnly) {
        return {column: true}
      }
      return {row: true}
    },
    creditor() {
      const member = this.collective.members.filter(
        user => user.id === this.liquidation.creditor)[0]
      return member
    },
    debtor() {
      const collective = this.$store.state.collective
      const member = collective.members.filter(
        user => user.id === this.liquidation.debtor)[0]
      return member
    },
    amount() {
      return Number(this.liquidation.amount.amount).toFixed(2)
    },
    isCreditor() {
      if (!this.selectedMember) {
        return false
      }
      return this.selectedMember.id === this.creditor.id
    },
    isDebtor() {
      if (!this.selectedMember) {
        return false
      }
      return this.selectedMember.id === this.debtor.id
    },
  },
}

</script>

<style scoped>

.no-grow {
  flex-grow: 0;
}

.text {
  align-self: flex-start;
}

.description {
  font-size: 1.5em;
}

.name {
  font-size: 2.5em;
}

.amount {
  font-size: 3em;
  font-weight: bold;
  align-self: flex-end;
  white-space: nowrap;
}

.avatar {
  max-width: 72px;
  max-height: 72px;
}

@media (max-width: 599px) {
  .description {
    font-size: 1.15em;
  }

  .name {
    font-size: 1.5em;
  }

  .amount {
    font-size: 1.75em;
  }

  .avatar {
    max-width: 64px;
    max-height: 64px;
  }
}

.currency {
  opacity: 0.25;
}

.liquidation-arrow {
  font-size: 5em;
  max-width: 24px;
  max-height: 24px;
}

</style>