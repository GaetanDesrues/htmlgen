import logging

import lorem
import pandas as pd
import treefiles as tf

from htmlit import HtmlGenerator


def main():
    rsc = tf.Tree.from_file(__file__, "rsc/rsc.tree")
    out_dir = tf.f(__file__) / "report"
    gen = HtmlGenerator()

    with gen.onglet("First Page"):
        gen.markdown("# Bienvenidos a todos", mt=20)
        gen.markdown(lorem.text())
        gen.vspace(50)
        with gen.row as r:
            r(0).markdown("### This is a row\n- List 1\n- *List 2*")
            r(0).latex(rf"\sum_i^n {__file__[10]}\left(i\right) = \mathbf(E)")
            r(0).markdown("That was an equation, like this one: $$x^2$$")
            r(0).markdown(lorem.paragraph())
            r(1).figure(rsc.img, "Healthy geometry + LBBB + biV pacing")

    with gen.onglet("Second page"):
        gen.vspace(20)
        gen.markdown(f"## {lorem.sentence()}")
        gen.markdown(lorem.paragraph())
        gen.markdown(f"## {lorem.sentence()}")
        with gen.row as r:
            r(0, "col-3").markdown("**First column (3)**")
            r(0).dataframe(pd.DataFrame({"A": [1, 2, 3], "B": [34, -1, 23]}))
            r(1, "col-2").markdown("*space (2)*")
            r(2, "col-5").markdown("**Second column (5)**")
            r(2).dataframe(pd.DataFrame({"C": [1, 2, 3], "D": [34, -1, 23]}))
        gen.markdown(f"## {lorem.sentence()}", mt=30)
        gen.markdown(lorem.text())
        gen.markdown(lorem.text())
        gen.markdown(lorem.text())

    with gen.onglet("Code"):
        gen.vspace(20)
        gen.markdown(f"## Code that generated this page")
        gen.code(tf.load_str(__file__))

    # Finally render html
    gen.render(out_dir, save_zip=True)


log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = tf.get_logger()

    main()
