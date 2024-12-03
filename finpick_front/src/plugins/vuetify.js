import { createVuetify } from 'vuetify';
import { VCard, VAvatar, VImg, VList, VListItem, VProgressLinear, VTextField, VBtn } from 'vuetify/components';
import { aliases, mdi } from 'vuetify/iconsets/mdi';
import 'vuetify/styles';

const vuetify = createVuetify({
  components: {
    VCard,
    VAvatar,
    VImg,
    VList,
    VListItem,
    VProgressLinear,
    VTextField,
    VBtn,
  },
  theme: {
    defaultTheme: 'light',
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
});

export default vuetify;