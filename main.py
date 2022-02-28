import logging

import pandas as pd
import treefiles as tf

from htmlit import HtmlGenerator


def main():
    rsc = tf.Tree.from_file(__file__, "rsc/rsc.tree")
    # print(rsc, rsc.img)

    gen = HtmlGenerator()

    with gen.row as r:
        r(0).markdown("# Hello\n- List 1\n- *List 2*")
        r(0).latex(rf"\sum_i^n {__file__[10]}\left(i\right) = \mathbf(E)")
        r(0).markdown("That was an equation, like this one: $$x^2$$")
        r(1).image(rsc.img)

    # gen.video(rsc.vid)

    with gen.row as r:
        r(0, "col-8").markdown("### First column (8)", mt=20)
        r(0).dataframe(pd.DataFrame({"A": [1, 2, 3], "B": [34, -1, 23]}))
        r(1, "col-4").markdown("### Second column (4)", mt=20)
        r(1).dataframe(pd.DataFrame({"C": [1, 2, 3], "D": [34, -1, 23]}))

    gen.render(tf.f(__file__) / "out", save_zip=True)


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    main()
