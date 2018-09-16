function tablify(dictionary, headName) {
  if (typeof dictionary === "object") {
    html =`
    <table>
    <thead>
    <tr>
      <th colspan="2">` + headName + "</th>" +`
    </tr>
    </thead>
    <tbody>\n`;
    for (var key in dictionary) {
      html += "<tr>\n";
      html += "  <td>" + key + "</td>\n";
      html += "  <td " + ( (typeof dictionary[key] === "object") ? 'class=\'table-inside\'' : '') + " >" + tablify(dictionary[key], key) + "</td>\n";
      html += "</tr>\n\n";
    }
    html += `
    </tbody>
    </table>`;
  } else {
    html = dictionary;
  }
  return html
}

function tablifylist(list, headName) {
  if (typeof list === "object") {
    html =`
    <table>
    <thead>
    <tr>
      <th colspan="2">` + headName + "</th>" +`
    </tr>
    </thead>
    <tbody>\n`;
    for (var i = 0; i < list.length; i++) {
      // Iterate over numeric indexes
      html += "<tr>\n";
      html += "  <td>" + list[i][0] + "</td>\n";
      html += "  <td " + ( (typeof list[i][1] === "object") ? 'class=\'table-inside\'' : '') + " >" + tablifylist(list[i][1], list[i][0]) + "</td>\n";
      html += "</tr>\n\n";
    }
    html += `
    </tbody>
    </table>`;
  }
  else {
    html = list;
  }

  return html
}

function tablifyshop(dictionary, headName) {
  if (typeof dictionary === "object") {
    html =`
    <table>
    <thead>
    <tr>
      <th colspan="2">` + headName + "</th>" +`
    </tr>
    </thead>
    <tbody>\n`;
    for (var key in dictionary) {
      var vals = [dictionary[key]['groupsize']];
      console.log(html);
      html += `
      <tr>\n
      <td>` + dictionary[key]['type'] + `</td>\n
      <td class='table-inside'>
      ` + table(vals, dictionary[key]['price']) + `
      </td>\n
      </tr>\n\n`;
    }
    html += `
    </tbody>
    </table>`;
  } else {
    html = dictionary;
  }
  return html
}

function table(list, headName) {
  html =`
  <table>
  <thead>
  <tr>
    <th colspan="0">` + headName + "</th>" +`
  </tr>
  </thead>
  <tbody>\n
    <tr>\n`;
  console.log(list);

    html += '    <td>' + list[0] + '</td>\n'

  html += `
    </tr>\n\n
  </tbody>
  </table>`;

  return html
}
