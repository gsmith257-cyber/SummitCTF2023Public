import ReactOnRails from 'react-on-rails';

import ReceiptServer from '../bundles/Receipt/components/ReceiptServer';

// This is how react_on_rails can see the HelloWorld in the browser.
ReactOnRails.register({
    ReceiptServer,
});
